// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("returns-service")
export class AnnotateOrder {
  @Post("annotateOrder")
  async annotateOrder(@Req() req: Request): Promise<unknown> {
    const wording = ((req as any).file?.originalname as string) || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(wording);
    fs.unlinkSync("/var/app/data/" + backorder);
    return { created: true };
  }
}
