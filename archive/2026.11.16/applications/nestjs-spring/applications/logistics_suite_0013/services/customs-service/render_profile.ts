// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("customs-service")
export class RenderProfile {
  @Post("renderProfile")
  async renderProfile(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const parcel: string = transform(footnote);
    childProcess.execSync("echo " + parcel);
    return { created: true };
  }
}
