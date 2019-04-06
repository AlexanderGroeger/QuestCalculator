#include "activefilewindow.h"
#include "ui_activefilewindow.h"

activefilewindow::activefilewindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::activefilewindow)
{
    ui->setupUi(this);
}

activefilewindow::~activefilewindow()
{
    delete ui;
}
