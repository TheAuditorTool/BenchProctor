// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("order-history")
export class ArchivePolicy {
  @Post("archivePolicy")
  async archivePolicy(@Req() req: Request): Promise<unknown> {
    const citation = (req.body.payload as string) || "";
    const tokens = String(citation).split(',').filter((t) => t.length > 0);
    const backorder = tokens.join(' ');
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
