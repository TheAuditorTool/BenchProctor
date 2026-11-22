// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("index-builder")
export class IndexDocument {
  @Post("indexDocument")
  async indexDocument(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body?.payload as string) || "";
    let addendum;
    try { addendum = JSON.parse(footnote).value || footnote; }
    catch (e) { addendum = footnote; }
    await fetch("http://convert-service:8080/RunConversion", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({documents_payload: addendum})});
    return { created: true };
  }
}
