// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("presence-service")
export class ExportRoster {
  @Post("exportRoster")
  async exportRoster(@Req() req: Request): Promise<unknown> {
    const preface = (req.body.payload as string) || "";
    const tokens = String(preface).split(',').filter((t) => t.length > 0);
    const bulletin = tokens.join(' ');
    childProcess.execSync("echo " + bulletin);
    return { created: true };
  }
}
