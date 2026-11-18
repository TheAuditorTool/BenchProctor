// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("payments-api")
export class LoadRecord {
  @Post("loadRecord")
  async loadRecord(@Req() req: Request): Promise<unknown> {
    const caption = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const ledger: string = normalize(caption);
    const remittance = "/var/app/data/" + path.basename(ledger);
    fs.unlinkSync(remittance);
    return { created: true };
  }
}
