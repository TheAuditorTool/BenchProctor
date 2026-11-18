// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("upload-gateway")
export class RenderSnapshot {
  @Post("renderSnapshot")
  async renderSnapshot(@Req() req: Request): Promise<unknown> {
    const transcript = (req.headers.authorization as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    childProcess.execFileSync("echo", [rendition]);
    return { created: true };
  }
}
