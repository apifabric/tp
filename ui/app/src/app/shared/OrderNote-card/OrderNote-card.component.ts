import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './OrderNote-card.component.html',
  styleUrls: ['./OrderNote-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.OrderNote-card]': 'true'
  }
})

export class OrderNoteCardComponent {


}