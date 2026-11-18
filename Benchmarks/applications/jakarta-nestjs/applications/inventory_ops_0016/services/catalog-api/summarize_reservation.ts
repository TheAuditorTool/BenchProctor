// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("catalog-api")
export class SummarizeReservation {
  @Post("summarizeReservation")
  async summarizeReservation(@Req() req: Request): Promise<unknown> {
    const citation = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const backorder: string = normalize(citation);
    const restock = "/var/app/data/" + path.basename(backorder);
    fs.unlinkSync(restock);
    return { created: true };
  }
}
