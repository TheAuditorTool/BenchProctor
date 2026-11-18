// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("catalog-api")
export class AnnotateAllocation {
  @Post("annotateAllocation")
  async annotateAllocation(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(phrase);
    childProcess.execSync("echo " + backorder);
    return { created: true };
  }
}
