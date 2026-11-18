// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("catalog-api")
export class LookupSku {
  @Post("lookupSku")
  async lookupSku(@Req() req: Request): Promise<unknown> {
    const memo = req.body.inventory_payload || "";
    const restock = "/var/app/data/" + path.basename(memo);
    fs.unlinkSync(restock);
    return { created: true };
  }
}
