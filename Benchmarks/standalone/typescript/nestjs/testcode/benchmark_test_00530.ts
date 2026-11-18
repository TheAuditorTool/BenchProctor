// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00530/:id")
  async BenchmarkTest00530(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const _raw = userInput;
    const data = (_raw && _raw.length > 0) ? _raw : 'default';
    const _sk = crypto.createHash("sha256").update(process.env.DATA_ENC_KEY || "").digest();
    const _siv = crypto.randomBytes(12);
    const _scipher = crypto.createCipheriv("aes-256-gcm", _sk, _siv);
    const _sct = Buffer.concat([_scipher.update(String(data), "utf8"), _scipher.final()]);
    const _stag = _scipher.getAuthTag();
    fs.writeFileSync("/var/data/cipher.bin", Buffer.concat([_siv, _stag, _sct]));
    return { created: true };
  }
}
