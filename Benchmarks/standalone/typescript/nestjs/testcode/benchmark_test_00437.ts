// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
import * as fs from "fs";
import * as crypto from "crypto";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00437")
  async BenchmarkTest00437(@Req() req: Request): Promise<unknown> {
    const userInput = (req.body as string) || "";
    const tokens = String(userInput).split(',').filter((t) => t.length > 0);
    const data = tokens.join(' ');
    const _sk = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY || "").digest();
    const _siv = crypto.randomBytes(12);
    const _scipher = crypto.createCipheriv("aes-256-gcm", _sk, _siv);
    const _sct = Buffer.concat([_scipher.update(String(data), "utf8"), _scipher.final()]);
    const _stag = _scipher.getAuthTag();
    fs.writeFileSync("/var/data/cipher.bin", Buffer.concat([_siv, _stag, _sct]));
    return { created: true };
  }
}
