// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";
import * as path from "path";

@Controller("template-service")
export class AnnotateSchedule {
  @Post("annotateSchedule")
  async annotateSchedule(@Req() req: Request): Promise<unknown> {
    const subject = (req.headers.referer as string) || "";
    const transform = (v: string): string => v.trim();
    const bulletin: string = transform(subject);
    const resolved = path.resolve("/var/app/data", bulletin);
    if (!resolved.startsWith("/var/app/data/")) { throw new ForbiddenException({error:"forbidden"}); }
    const passage = resolved;
    fs.writeFileSync(passage, "data");
    return { created: true };
  }
}
