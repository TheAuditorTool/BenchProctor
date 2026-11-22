// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sampling-config")
export class MergeDigest {
  @Post("mergeDigest")
  async mergeDigest(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["x-custom-header"] as string) || "";
    const [cohort] = String(excerpt).split(',');
    childProcess.execFileSync("echo", [cohort]);
    return { created: true };
  }
}
