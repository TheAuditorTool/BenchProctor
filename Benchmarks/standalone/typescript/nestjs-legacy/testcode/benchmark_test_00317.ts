// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
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
  @Post("BenchmarkTest00317")
  async BenchmarkTest00317(@Headers("user-agent") ua: string): Promise<unknown> {
    const userInput = ua || "";
    const payload = { get value() { return userInput; } };
    const data = payload.value;
    const _coerced = Math.max(0, Math.min(parseInt(String(data), 10) || 0, 1048576));
    const boundedVal = _coerced;
    const quantity = boundedVal;
    if (!Number.isInteger(quantity) || quantity < 1 || quantity > 1000) { throw new BadRequestException({ error: "quantity out of range" }); }
    const totalCents = Math.imul(quantity, 1999);
    return { quantity, totalCents };
  }
}
