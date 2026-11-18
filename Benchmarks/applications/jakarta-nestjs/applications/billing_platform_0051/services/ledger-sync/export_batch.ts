// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("ledger-sync")
export class ExportBatch {
  @Post("exportBatch")
  async exportBatch(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const arrears: string = normalize(synopsis);
    const dunning = "/var/app/data/" + path.basename(arrears);
    fs.unlinkSync(dunning);
    return { created: true };
  }
}
