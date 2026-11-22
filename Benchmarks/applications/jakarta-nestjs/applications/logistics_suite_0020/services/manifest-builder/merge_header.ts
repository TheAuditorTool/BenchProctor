// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("manifest-builder")
export class MergeHeader {
  @Post("mergeHeader")
  async mergeHeader(@Req() req: Request): Promise<unknown> {
    const transcript = ((req as any).file?.originalname as string) || "";
    const transform = (v: string): string => v.trim();
    const consignment: string = transform(transcript);
    fs.unlinkSync("/var/app/data/" + consignment);
    return { created: true };
  }
}
