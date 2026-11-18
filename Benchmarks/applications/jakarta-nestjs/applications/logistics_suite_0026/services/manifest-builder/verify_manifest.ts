// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("manifest-builder")
export class VerifyManifest {
  @Post("verifyManifest")
  async verifyManifest(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    let parcel;
    try { parcel = JSON.parse(citation).value || citation; }
    catch (e) { parcel = citation; }
    JSON.parse(parcel);
    return { created: true };
  }
}
