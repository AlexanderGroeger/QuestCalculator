#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->file_select_button1,SIGNAL(clicked()),this,SLOT(on_FileSelectButton1_clicked()));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_FileSelectButton1_clicked()
{
    ui->file_select_page->hide();
    ui->active_file_page->show();
}
