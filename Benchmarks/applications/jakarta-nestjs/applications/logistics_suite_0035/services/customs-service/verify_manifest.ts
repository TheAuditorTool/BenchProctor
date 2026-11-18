// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("customs-service")
export class VerifyManifest {
  @Post("verifyManifest")
  async verifyManifest(@Req() req: Request): Promise<unknown> {
    const phrase = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const parcel: string = normalize(phrase);
    await db.query("SELECT * FROM users WHERE id = $1", [parcel]);
    return { created: true };
  }
}
