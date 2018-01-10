import { Component, ViewChild } from '@angular/core';
import { PickedFile } from 'angular-file-picker';
import { SignaturePad } from 'angular2-signaturepad/signature-pad';

declare var $ : any


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent {
  title = 'app';

  selectedFile : String

  firstname : String
  lastname : String
  street : String
  streetnumber : String
  plz : String
  wohnort : String
  email : String
  

  @ViewChild(SignaturePad) signaturePad: SignaturePad;

  filePicked(event : PickedFile) {
    this.selectedFile = event.content
  }

  onSignatureSave(event) {
    console.log(event)
  }

  submit() {
    let signatureUrl = this.signaturePad.toDataURL()
    $('.modal').modal()
    $('.modal').modal('open');
    }


}
