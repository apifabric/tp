import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrderNoteHomeComponent } from './home/OrderNote-home.component';
import { OrderNoteNewComponent } from './new/OrderNote-new.component';
import { OrderNoteDetailComponent } from './detail/OrderNote-detail.component';

const routes: Routes = [
  {path: '', component: OrderNoteHomeComponent},
  { path: 'new', component: OrderNoteNewComponent },
  { path: ':id', component: OrderNoteDetailComponent,
    data: {
      oPermission: {
        permissionId: 'OrderNote-detail-permissions'
      }
    }
  }
];

export const ORDERNOTE_MODULE_DECLARATIONS = [
    OrderNoteHomeComponent,
    OrderNoteNewComponent,
    OrderNoteDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class OrderNoteRoutingModule { }