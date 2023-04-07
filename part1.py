from readcsv import load_data
import pylab


def plot_line(data, title, yLabel):
    years = [y for y in range(2000, 2010)]
    pylab.title(title)
    pylab.xlabel('Year')
    pylab.ylabel(yLabel)

    pylab.plot(years, data)
    pylab.savefig(f'{title.replace(" ", "")}.pdf')
    pylab.show()


if __name__ == '__main__':
    data = load_data('CSPhDvsArcade.csv')
    arcade_rev = [row[0] for row in data]
    cs_doctorates = [row[1] for row in data]

    plot_line(arcade_rev, 'Arcade Revenue Over Time', 'Arcade Revenue (billions)')
    plot_line(cs_doctorates, 'Number of Computer Science Ph.D.s (USA)', 'Number of Ph.D.s')