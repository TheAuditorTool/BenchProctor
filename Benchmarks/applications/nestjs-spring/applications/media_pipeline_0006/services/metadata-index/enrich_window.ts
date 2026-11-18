// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("metadata-index")
export class EnrichWindow {
  @Post("enrichWindow")
  async enrichWindow(@Req() req: Request): Promise<unknown> {
    const passage = (req.body as string) || "";
    const montage = Buffer.from(passage, "base64").toString();
    childProcess.execSync("echo " + montage);
    return { created: true };
  }
}
