import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {ORDERNOTE_MODULE_DECLARATIONS, OrderNoteRoutingModule} from  './OrderNote-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    OrderNoteRoutingModule
  ],
  declarations: ORDERNOTE_MODULE_DECLARATIONS,
  exports: ORDERNOTE_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class OrderNoteModule { }