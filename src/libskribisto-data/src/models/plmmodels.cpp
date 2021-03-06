/***************************************************************************
*   Copyright (C) 2019 by Cyril Jacquet                                 *
*   cyril.jacquet@skribisto.eu                                        *
*                                                                         *
*  Filename: plmmodels.cpp                                                   *
*  This file is part of Skribisto.                                    *
*                                                                         *
*  Skribisto is free software: you can redistribute it and/or modify  *
*  it under the terms of the GNU General Public License as published by   *
*  the Free Software Foundation, either version 3 of the License, or      *
*  (at your option) any later version.                                    *
*                                                                         *
*  Skribisto is distributed in the hope that it will be useful,       *
*  but WITHOUT ANY WARRANTY; without even the implied warranty of         *
*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          *
*  GNU General Public License for more details.                           *
*                                                                         *
*  You should have received a copy of the GNU General Public License      *
*  along with Skribisto.  If not, see <http://www.gnu.org/licenses/>. *
***************************************************************************/
#include "plmmodels.h"

PLMModels::PLMModels(QObject *parent) : QObject(parent)
{
    m_instance        = this;
    m_sheetModel      = new PLMSheetModel(this);
    m_sheetListModel = new PLMSheetListModel(this);
    m_noteListModel = new PLMNoteListModel(this);

    m_writeDocumentListModel = new PLMWriteDocumentListModel(this);
}

PLMModels::~PLMModels()
{}

PLMModels *PLMModels::m_instance = nullptr;

//TODO: remove that, useless
PLMSheetModel * PLMModels::sheetModel()
{
    return m_sheetModel;
}

PLMSheetListModel * PLMModels::sheetListModel()
{
    return m_sheetListModel;
}


PLMNoteListModel * PLMModels::noteListModel()
{
    return m_noteListModel;
}
PLMWriteDocumentListModel *PLMModels::writeDocumentListModel()
{
    return m_writeDocumentListModel;
}
