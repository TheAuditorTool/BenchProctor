// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("secret-broker")
export class NormalizeFlag {
  @Post("normalizeFlag")
  async normalizeFlag(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers.authorization as string) || "";
    const transform = (v: string): string => v.trim();
    const persona: string = transform(passage);
    return "<div>" + persona + "</div>";
  }
}
