// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("delivery-service")
export class ArchiveReceipt {
  @Post("archiveReceipt")
  async archiveReceipt(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers["x-custom-header"] as string) || "";
    const [bulletin] = String(preface).split(',');
    childProcess.execFileSync("echo", [bulletin]);
    return { created: true };
  }
}
