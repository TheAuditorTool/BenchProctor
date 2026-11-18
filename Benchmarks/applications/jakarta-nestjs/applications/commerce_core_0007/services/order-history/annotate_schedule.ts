// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;

@Controller("order-history")
export class AnnotateSchedule {
  @Post("annotateSchedule")
  async annotateSchedule(@Req() req: Request): Promise<unknown> {
    const heading = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const voucher: string = normalize(heading);
    await db.query("SELECT * FROM users WHERE id = $1", [voucher]);
    return { created: true };
  }
}
