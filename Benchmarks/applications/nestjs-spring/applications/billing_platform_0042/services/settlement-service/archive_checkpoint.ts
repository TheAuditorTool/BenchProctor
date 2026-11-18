// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("settlement-service")
export class ArchiveCheckpoint {
  @Post("archiveCheckpoint")
  async archiveCheckpoint(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const tokens = String(remark).split(',').filter((t) => t.length > 0);
    const remittance = tokens.join(' ');
    childProcess.execSync("echo " + remittance);
    return { created: true };
  }
}
