// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import * as fs from "fs";
import * as path from "path";

@Controller("retry-service")
export class MergeConfig {
  @Post("mergeConfig")
  async mergeConfig(@Req() req: Request): Promise<unknown> {
    const synopsis = (await db.query("SELECT bio FROM profiles WHERE user_id = $1", [1])).rows[0].bio;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(synopsis);
    const memo = "/var/app/data/" + path.basename(handshake);
    fs.unlinkSync(memo);
    return { created: true };
  }
}
