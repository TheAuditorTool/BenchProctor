// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("thumbnail-service")
export class EnrichThreshold {
  @Post("enrichThreshold")
  async enrichThreshold(@Req() req: Request): Promise<unknown> {
    const snippet = (req.body as string) || "";
    const tokens = String(snippet).split(',').filter((t) => t.length > 0);
    const montage = tokens.join(' ');
    childProcess.spawn("echo " + montage, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
