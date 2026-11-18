// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("payments-api")
export class AnnotateSnapshot {
  @Post("annotateSnapshot/:id")
  async annotateSnapshot(@Req() req: Request): Promise<unknown> {
    const subject = (req.params.id as string) || "";
    const transform = (v: string): string => v.trim();
    const ledger: string = transform(subject);
    return "<div>" + ledger + "</div>";
  }
}
