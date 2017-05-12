from PollyReports import *
from reportlab.pdfgen.canvas import Canvas

'''This program defines two functions for pdf generation and report generation'''
def _Sched(directory, data):
    #Creates empty pdf file at selected directory
    hndle = open(directory, 'w')
    hndle.close()
    #makes a report objecy
    report = Report(data)
    report.detailband = Band([
    #adds columns to the report based on data
        Element((72, 0), ('Helvetica', 12), key = 0),
        Element((200, 0), ('Helvetica', 12), key = 1),
        Element((272, 0), ('Helvetica', 12), key = 2),
        Element((344, 0), ('Helvetica', 12), key = 3),
        Element((416, 0), ('Helvetica', 12), key = 4),
        Element((488, 0), ('Helvetica', 12), key = 5),
        Element((544, 0), ('Helvetica', 12), key = 6),
        Element((600, 0), ('Helvetica', 12), key = 7),
        Rule((65, 20), 8 * 72, thickness = 1)
    ])

    report.pageheader = Band([
    #sets up the page header and moves around the elements
        Element((36, 0), ('Times-Bold', 24), text = 'Schedule'),
        Element((72, 65), ('Helvetica', 12), text = 'Name'),
        Element((200, 65), ('Helvetica', 12), text = 'Monday'),
        Element((272, 65), ('Helvetica', 12), text = 'Tuesday'),
        Element((344, 65), ('Helvetica', 12), text = 'Wednesday'),
        Element((416, 65), ('Helvetica', 12), text = 'Thursday'),
        Element((488, 65), ('Helvetica', 12), text = 'Friday'),
        Element((544, 65), ('Helvetica', 12), text = 'Saturday'),
        Element((600, 65), ('Helvetica', 12), text = 'Sunday'),
        Rule((36, 80), 72 * 8.5, thickness = 2),
    ])

    report.pagefooter = Band([
    #adds the page number to the end of the page
        Element((36, 0), ('Helvetica-Bold', 12),
            sysvar = 'pagenumber',
            format = lambda x: 'Page %d' % x),
    ])

    #makes a canvas object for writing to a file
    canvas = Canvas(directory, (72 * 11, 72 * 8.5))
    #add report to pdf
    report.generate(canvas)
    #save the pdf
    canvas.save()

def _Atten(directory, data):
#function that adds a graph to a pdf
    from reportlab.graphics import renderPDF
    from reportlab.graphics.shapes import Drawing
    from reportlab.graphics.charts.lineplots import LinePlot
    from reportlab.graphics.widgets.markers import makeMarker

    hndle = open(directory, 'w')
    hndle.close()
#makes a graph and sets up the axis and line based on the inputted data
    drawing = Drawing(72 * 11, 72 * 8.5)
    lp = LinePlot()
    lp.x = 36
    lp.y = 36
    lp.height = 72 * 7.5
    lp.width = 720
    lp.data = data
    lp.lines[0].symbol = makeMarker('FilledCircle')
    lp.xValueAxis.valueMin = 8
    lp.xValueAxis.valueMax = 23
    lp.xValueAxis.valueSteps = [x for x in range(8, 24)]
    drawing.add(lp)
    canvas = Canvas(directory, (72 * 11, 72 * 8.5))
    renderPDF.draw(drawing, canvas, 0, 0)
    canvas.showPage()
    canvas.save()
