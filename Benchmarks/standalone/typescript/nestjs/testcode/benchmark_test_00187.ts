// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post, Req } from "@nestjs/common";
import { Request, Response } from "express";
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
  @Post("BenchmarkTest00187/:id")
  async BenchmarkTest00187(@Param("id") pathId: string, @Req() req: Request): Promise<unknown> {
    const userInput = pathId;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    const _coerced = parseFloat(String(data));
    const parsedNum = _coerced;
    req.session.data = String(parsedNum);
    return { created: true };
  }
}
