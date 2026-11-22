// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("statement-export")
export class BuildStatement {
  @Post("buildStatement/:id")
  async buildStatement(@Req() req: Request): Promise<unknown> {
    const headline = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(headline);
    await fetch("http://refund-service:8080/IssueRefund", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({billing_payload: remittance})});
    return { created: true };
  }
}
