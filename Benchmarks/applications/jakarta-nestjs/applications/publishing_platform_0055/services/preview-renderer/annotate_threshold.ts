// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("preview-renderer")
export class AnnotateThreshold {
  @Post("annotateThreshold")
  async annotateThreshold(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers["x-custom-header"] as string) || "";
    const [byline] = String(synopsis).split(',');
    childProcess.execFileSync("echo", [byline]);
    return { created: true };
  }
}
