import datetime


class Chart:
    def __init__(self, dataset):
        self.dataset = dataset
        self.maxY = 0

        self.width = 992
        self.height = 300

        self.margin_left = 100
        self.margin_top = 24
        self.margin_bottom = 32
        self.font = "Sans serif"

        self._autoscale()

    def _autoscale(self):
        for point in self.dataset:
            if point[1] > self.maxY:
                self.maxY = point[1]

        if self.maxY < 500:
            self.maxY = ((self.maxY // 10) + 1) * 10

    def _generate_axes(self):
        result = []
        bottom = self.height - self.margin_bottom
        result.append(
            '<line x1="{0}.5" y1="{1}.5" x2="{0}.5" y2="{2}.5" stroke="black" />'.format(self.margin_left,
                                                                                         self.margin_top,
                                                                                         bottom))
        result.append(
            '<line x1="{0}.5" y1="{1}.5" x2="{2}.5" y2="{1}.5" stroke="black" />'.format(self.margin_left, bottom,
                                                                                         self.width))

        result.append(
            '<text transform="translate({x} {y}) rotate(90)" class="axes-label" font-family="{font}">{text}</text>'.format(
                x=self.margin_left + 5,
                y=self.margin_top + 5,
                text="Devices",
                font=self.font
            ))

        result.append(
            '<text x="{x}" y="{y}" class="axes-label" text-anchor="end" font-family="{font}">{text}</text>'.format(
                x=self.width - 5,
                y=bottom - 5,
                text="Days",
                font=self.font))

        return result

    def _generate_ticks(self):
        result = []
        chart_width = self.width - self.margin_left
        chart_height = self.height - self.margin_top - self.margin_bottom

        yticks = (chart_height // 24) - 1
        for idx, value in enumerate(range(0, self.maxY + 1, int(self.maxY / yticks))):
            position = int(chart_height + self.margin_top - (idx * (chart_height // yticks)))
            if value > 0:
                result.append(
                    '<line x1="{0}.5" y1="{1}.5" x2="{2}.5" y2="{1}.5" stroke="#ccc" />'.format(self.margin_left,
                                                                                                position,
                                                                                                self.width))
            result.append(
                '<text x="{x}" y="{y}" text-anchor="end" class="axes-tick" font-family="{font}" font-size="0.8em">{value}</text>'.format(
                    value=value,
                    x=self.margin_left - 5,
                    y=position + 5,
                    font=self.font))

        xticks = (chart_width // 65) - 1
        lastyear = ""
        for idx in range(0, xticks):
            dataset_idx = (len(self.dataset) // xticks) * idx
            year, month, day = self.dataset[dataset_idx][0].split('-')
            value = datetime.datetime(year=int(year), month=int(month), day=int(day))

            position = self.margin_left + (chart_width // xticks) * idx
            result.append(
                '<text x="{x}" y="{y}" class="axes-tick" font-family="{font}" font-size="0.8em">{value:%b}</text>'.format(
                    value=value,
                    x=position,
                    y=chart_height + self.margin_top + 15,
                    font=self.font))
            if lastyear != year:
                lastyear = year
                result.append(
                    '<text x="{x}" y="{y}" class="axes-tick" font-family="{font}" font-size="0.8em">{value}</text>'.format(
                        value=year,
                        x=position,
                        y=chart_height + self.margin_top + 32,
                        font=self.font))

        return result

    def _generate_line(self):
        chart_width = self.width - self.margin_left
        chart_height = self.height - self.margin_top - self.margin_bottom
        coordinates = []
        yscale = chart_height / self.maxY
        xscale = chart_width / (len(self.dataset) - 1)

        for idx, point in enumerate(self.dataset):
            x = (idx * xscale) + self.margin_left
            y = chart_height - (point[1] * yscale) + self.margin_top
            coordinates.append("{},{}".format(x, y))

        return '<polyline points="{}" fill="none" stroke="#009900" />'.format(' '.join(coordinates))

    def generate(self):
        result = []
        result.append(
            '<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">'.format(
                width=self.width, height=self.height))
        result.extend(self._generate_ticks())
        result.extend(self._generate_axes())
        result.append(self._generate_line())
        result.append('</svg>')
        return '\n'.join(result)


if __name__ == '__main__':
    import json

    with open('../dataset.json') as handle:
        dataset = json.load(handle)
    test = Chart(dataset)
    with open('test.svg', 'w') as handle:
        handle.write(test.generate())
