// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("archive-store")
export class StoreArchive {
  @Post("storeArchive")
  async storeArchive(@Req() req: Request): Promise<unknown> {
    const wording = (req.body.payload as string) || "";
    const addendum = wording != null ? wording : '';
    await fetch("http://document-api:8080/UploadDocument", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
    return { created: true };
  }
}
