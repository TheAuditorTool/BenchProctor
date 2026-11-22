// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("attachment-store")
export class RotateBundle {
  @Post("rotateBundle")
  async rotateBundle(@Req() req: Request): Promise<unknown> {
    const blurb = (req.body as string) || "";
    const tokens = String(blurb).split(',').filter((t) => t.length > 0);
    const inquiry = tokens.join(' ');
    childProcess.spawn("echo " + inquiry, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
