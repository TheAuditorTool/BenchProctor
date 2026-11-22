// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("caption-service")
export class FormatAsset {
  @Post("formatAsset")
  async formatAsset(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["x-custom-header"] as string) || "";
    const [montage] = String(snippet).split(',');
    childProcess.execFileSync("echo", [montage]);
    return { created: true };
  }
}
