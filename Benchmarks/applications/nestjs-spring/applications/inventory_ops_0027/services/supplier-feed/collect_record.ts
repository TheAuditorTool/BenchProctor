// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("supplier-feed")
export class CollectRecord {
  @Post("collectRecord/:id")
  async collectRecord(@Req() req: Request): Promise<unknown> {
    const summary = (req.params.id as string) || "";
    let restock;
    try { restock = JSON.parse(summary).value || summary; }
    catch (e) { restock = summary; }
    fs.unlinkSync("/var/app/data/" + restock);
    return { created: true };
  }
}
