// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("attachment-store")
export class EnrichCheckpoint {
  @Post("enrichCheckpoint/:id")
  async enrichCheckpoint(@Req() req: Request): Promise<unknown> {
    const remark = (req.params.id as string) || "";
    let inquiry;
    try { inquiry = JSON.parse(remark).value || remark; }
    catch (e) { inquiry = remark; }
    fs.unlinkSync("/var/app/data/" + inquiry);
    return { created: true };
  }
}
