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
    # data = load_data('CSPhDvsArcade.csv')
    data = load_data('Cigarettes_AgeLived.csv')
    x = [row[0] for row in data]
    y = [row[1] for row in data]
    title = 'Cigarettes Smoked vs. Age Lived'
    pylab.title(title)
    pylab.xlabel('Cigarettes Smoked')
    pylab.ylabel('Age Lived')

    pylab.plot(x, y, 'bo')
    pylab.savefig(f'{title.replace(" ", "")}.pdf')
    pylab.show()
    # plot_line(x, 'Arcade Revenue Over Time', 'Arcade Revenue (billions)')
    # plot_line(y, 'Number of Computer Science Ph.D.s (USA)', 'Number of Ph.D.s')
