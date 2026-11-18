// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("redaction-service")
export class PublishRoster {
  @Post("publishRoster")
  async publishRoster(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const dossier: string = transform(excerpt);
    childProcess.execSync("echo " + dossier);
    return { created: true };
  }
}
