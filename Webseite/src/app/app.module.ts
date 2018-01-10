import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { ListComponent } from "./ListComponent/list.component";
import { HttpClientModule } from '@angular/common/http';
import { CommService } from './Services/comm.service';

import { AngularFilePickerModule } from 'angular-file-picker';

import { SignaturePadModule } from 'angular2-signaturepad';

import { FormsModule } from '@angular/forms';
import { ModelService } from './Services/model.service';


@NgModule({
  declarations: [
    AppComponent,
    ListComponent,
    ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AngularFilePickerModule,
    SignaturePadModule,
    FormsModule
  ],
  providers: [
    CommService,
    ModelService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
