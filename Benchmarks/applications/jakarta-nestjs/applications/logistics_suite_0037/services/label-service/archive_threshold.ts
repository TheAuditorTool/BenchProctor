// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("label-service")
export class ArchiveThreshold {
  @Post("archiveThreshold")
  async archiveThreshold(@Req() req: Request): Promise<unknown> {
    const footnote = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const consignment: string = normalize(footnote);
    await db.query("SELECT * FROM users WHERE id = $1", [consignment]);
    return { created: true };
  }
}
