// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00042")
  async BenchmarkTest00042(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const data = String(userInput).split(/[ \t]+/).join(" ");
    const requested = parseInt(data, 10);
    const wrapped = (requested + 1) | 0;
    const buf = Buffer.alloc(wrapped);
    return { allocated: buf.length };
  }
}
