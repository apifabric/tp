import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ItemHomeComponent } from './home/Item-home.component';
import { ItemNewComponent } from './new/Item-new.component';
import { ItemDetailComponent } from './detail/Item-detail.component';

const routes: Routes = [
  {path: '', component: ItemHomeComponent},
  { path: 'new', component: ItemNewComponent },
  { path: ':id', component: ItemDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Item-detail-permissions'
      }
    }
  },{
    path: ':item_id/Return', loadChildren: () => import('../Return/Return.module').then(m => m.ReturnModule),
    data: {
        oPermission: {
            permissionId: 'Return-detail-permissions'
        }
    }
}
];

export const ITEM_MODULE_DECLARATIONS = [
    ItemHomeComponent,
    ItemNewComponent,
    ItemDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ItemRoutingModule { }