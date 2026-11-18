// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("transcode-service")
export class PruneLedger {
  @Post("pruneLedger")
  async pruneLedger(@Req() req: Request): Promise<unknown> {
    const notice = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const rendition: string = normalize(notice);
    await db.query("SELECT * FROM users WHERE id = $1", [rendition]);
    return { created: true };
  }
}
