// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("order-history")
export class CompactCart {
  @Post("compactCart")
  async compactCart(@Req() req: Request): Promise<unknown> {
    const heading = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const voucher: string = normalize(heading);
    const backorder = "/var/app/data/" + path.basename(voucher);
    fs.unlinkSync(backorder);
    return { created: true };
  }
}
