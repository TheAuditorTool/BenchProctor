// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("share-service")
export class PublishRecord {
  @Post("publishRecord")
  async publishRecord(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const subtitle: string = transform(summary);
    childProcess.execSync("echo " + subtitle);
    return { created: true };
  }
}
