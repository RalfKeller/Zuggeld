import { Component, ViewChild } from '@angular/core';
import { PickedFile } from 'angular-file-picker';
import { SignaturePad } from 'angular2-signaturepad/signature-pad';
import { CommService } from './Services/comm.service';
import { ModelService } from './Services/model.service';

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
  anrede : String = "Herr"
  land : String
  agbAkzeptiert : boolean
  

  @ViewChild(SignaturePad) signaturePad: SignaturePad;

  constructor(private commService : CommService, private modelService : ModelService) {}

  filePicked(event : PickedFile) {
    this.selectedFile = event.content
  }

  onSignatureSave(event) {
    console.log(event)
  }

  submit() {
    let signatureUrl = this.signaturePad.toDataURL()
    console.log(signatureUrl)
    console.log(this.anrede)

    let user : User = {
      anrede: this.anrede,
      vorname: this.firstname,
      name: this.lastname,
      strasse: this.street,
      strasse_nr: this.streetnumber,
      staat: this.land,
      plz: this.plz,
      wohnort: this.wohnort,
      konto_inhaber: "",
      iban: "",
      bic: "",
      datum_unterschrift: Date.now().toString(),
      unterschrift: signatureUrl,
      ticket_bild: this.selectedFile,
      mail: this.email
    }

    this.commService.postData(user, this.modelService.getSelectedDelays().map((delay) => {return +delay.id; }));

    if(!this.selectedFile || !this.firstname || !this.lastname || !this.street || !this.streetnumber
    || !this.plz || !this.wohnort || !this.email || !this.land || !this.agbAkzeptiert ) {
      $('#errorModal').modal()
      $('#errorModal').modal('open');
    }

    else {
      $('#doneModal').modal()
      $('#doneModal').modal('open');
    }
    }


}
